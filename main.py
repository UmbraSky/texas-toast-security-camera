#####################################################################################
# Team Name: Texas Toast                                                            #
# Members: Ryan Saffel, Brie Bays, Austin Newsom, Elora Browning                    #
# Date: 4/19/2023                                                                   #
# Description: Hidden Security Camera                                               #
#####################################################################################
#import TTSecurityCam_bot
from flask import Flask, session, request, g
from app import gui_bp

theApp = Flask(__name__)
theApp.secret_key = "jlsak6jfl4kasj121fllhi"
theApp.register_blueprint(gui_bp)

app_ctx = theApp.app_context()
app_ctx.push()


with theApp.app_context():
    import app


#ALERT_SYSTEM_FLAG = False
#if ALERT_SYSTEM_FLAG == True:
#    TTSecurityCam_bot


while True:
    app.runGUI()



