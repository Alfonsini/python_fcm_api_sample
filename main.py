from fcm_utils import FcmUtils

def main():
    messaging = FcmUtils()
    messaging.send_to_token(
        registration_token='d2cdv7LJ407RhmCXknDi1m:APA91bEUT8UTNs9i8NG-bfAp5jv46MKkiob7cXrQ-XnxXS194bxQOD1NC1maN05czlhj9f0e8DHuI8nLG5lv6n0KnRQbIvn2OIkbpBg7E-ALSmT5fqPPoPP-Sev48FYEMToB0y_CRJ4X',
        title='title',
        body='body from topic',
        data={
            'content-available':'1',
            'notification_body' : 'Data message body',
            'notification_title': 'Data message title',
            'notification_foreground': 'true',
            # 'notification_ios_sound': 'default',
            'notification_ios_badge': '1',
            'key_1' : 'Data for key one'            
        },
        image='https://picsum.photos/200/300',
        click_action='FCM_PLUGIN_ACTIVITY',
        priority='normal',
        sound_filename='alert',
        category= 'news'
    )
    
    # messaging.send_to_topic("topics-all", "title", "body from topic")

if __name__ == "__main__":
    main()