from app_config  import AppConfig
from application import Application

if __name__ == "__main__":

    config = AppConfig().get_arguments()
    app    = Application ( config )
    
    app.run()