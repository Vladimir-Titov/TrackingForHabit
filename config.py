import envparse

envparse.env.read_envfile('.env')

dsn = envparse.env('dsn', default=str)
