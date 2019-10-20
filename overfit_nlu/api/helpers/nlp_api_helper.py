from api import interpreter, last_status, information, start_time
import datetime
# dictionary = {'greet': 'D:/PycharmProjects/audioset_classification-master/audio/chao.wav',
#               'booking_query': 'D:/PycharmProjects/audioset_classification-master/audio/phòng băng cốc.wav',
#               'interview_time': 'bạn có lịch hẹn lúc mấy giờ vậy.wav',
#               'interview_guest_name': 'bạn cho mình xin tên ạ.wav',
#               'interview_responsibility': 'ban_can_lien_he_voi_ai.wav',
#               'interview_query_complete': 'minh_da_lien_he.wav',
#               'company_office_query': '3_van_phong.wav',
#               'company_aspect_query': 'sun lam viec trong cac linh vuc.wav',
#               'company_workingtime_query': 'sun làm việc từ.wav',
#               }
def processing(message):
  print(message)
  global last_status, information, start_time
  if datetime.datetime.now().timestamp() - start_time.timestamp() > 5:
    with open('D:\PycharmProjects\overfit_nlu\static\status.txt', 'w') as f:
      start_time = datetime.datetime.now()
      # message = preprocess(message)
      nlu_response = interpreter.parse(message)
      if last_status == 0:
        information = {}
        if nlu_response['intent']['confidence'] > 0.5:
          intent = nlu_response['intent']['name']
          if intent == 'interview_query':
            last_status = 1
            entities = nlu_response['entities']
            for entity in entities:
              if entity['entity'] == 'time':
                information['time'] = entity['value']
                f.write('interview_guest_name')
                return 'interview_guest_name'
            f.write('interview_time')
            return 'interview_time'
          else:
            last_status = 0
        else:
          intent = 'other'
          last_status = 0
        f.write(intent)
        return intent
      else:
        if 'time' not in information:
          information['time'] = message
          f.write('interview_guest_name')
          return 'interview_guest_name'
        if 'guest_name' not in information:
          information['guest_name'] = message
          f.write('interview_responsibility')
          return 'interview_responsibility'
        elif 'responsibility' not in information:
          information['responsibility'] = message
          last_status = 0
          f.write('interview_query_complete')
          return 'interview_query_complete'
  else:
    return 'noise'
