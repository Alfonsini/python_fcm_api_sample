from fcm_utils import FcmUtils

def main():
    messaging = FcmUtils()
    messaging.send_to_token(
        registration_token='',
        title='title',
        body='body from topic',
        data={'content-available':'1'},
        image='https://picsum.photos/200/300',
        click_action='FCM_PLUGIN_ACTIVITY',
        priority='normal',
        # sound_filename='alert.mp3',
    )
    
    # messaging.send_to_topic("topics-all", "title", "body from topic")

if __name__ == "__main__":
    main()