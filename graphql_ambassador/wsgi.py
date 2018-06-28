import os
import graphql_ambassador

port = int(os.getenv("PORT", 5000))
env = os.getenv("AMBASSADOR_ENV", "DEVELOPMENT")
environment = graphql_ambassador.Environment.from_string(env)
app = graphql_ambassador.create_app(environment)

if __name__ == "__main__":
    app.run(port=port)
