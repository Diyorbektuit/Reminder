import environ

env = environ.Env()
env.read_env(".env")

BOT_TOKEN = env.str("BOT_TOKEN", None)
print(BOT_TOKEN)