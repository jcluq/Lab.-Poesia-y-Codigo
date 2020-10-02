import tweepy
import time
from configuracion import Configuracion


class Tweetest:
    def __init__(self):
        # corre el API y verifica las llaves de acceso
        self.configuracion = Configuracion()
        auth = tweepy.OAuthHandler(self.configuracion.api_key, self.configuracion.secret_api_key)
        auth.set_access_token(self.configuracion.access_token, self.configuracion.secret_access_token)
        self.api = tweepy.API(auth)
        self.bandera_autentificacion = self.api.verify_credentials()

    def _seguir_seguidores(self):
        # Esta funcion sigue a quienes nos sigan
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                follower.follow()

    def responder_tweets(self, palabras, since_id):
        # Responde los tweets donde se nos etiquete
        new_since_id = since_id
        for tweet in tweepy.Cursor(self.api.mentions_timeline,
                                   since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            if any(palabra in tweet.text.lower() for palabra in palabras):
                # Seguimos a quien nos etiquete si aun no se le sigue
                if not tweet.user.following:
                    tweet.user.follow()
                usuarix = tweet.user.screen_name
                respuesta = "Bot-Respondiendole a " + "@" + str(usuarix)
                self.api.update_status(
                    status=respuesta,
                    in_reply_to_status_id=tweet.id,
                )
        return new_since_id

    def programa(self):
        # Aca es donde corren todas las funciones
        # Revisa que las llaves este correctas para empezar a correr
        if self.bandera_autentificacion is not False:
            print('Autentificacion correcta')
            since_id = 1
            while True:
                # Aca se responden los tweets si alguno de los caracteres en parentesis se encuentra
                # En este caso la palabra 'respuesta' o un espacio ' '
                since_id = self.responder_tweets([" ", "respuesta"], since_id)
                self._seguir_seguidores()
                time.sleep(10)
                print('zas, iteracion')


test = Tweetest()
test.programa()
