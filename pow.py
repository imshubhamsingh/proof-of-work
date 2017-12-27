
from datetime import datetime as dt
import hashlib


def proof_of_work(bloockdata, difficulty):
    nounce = 'NOT-FOUND'
    startTime = dt.now()
    endTime = startTime
    tryNounce = 0

    while tryNounce < 10000000:
        newData = bloockdata + str(tryNounce)
        sha = hashlib.sha256()
        sha.update(newData.encode('utf-8'))
        if sha.hexdigest().startswith(difficulty):
            endTime = dt.now()
            nounce = tryNounce
            break
        tryNounce+=1

    timetaken = endTime - startTime
    if timetaken == 0:
        print ('Difficulty=', difficulty, ' Nounce not found!!!!')
    else:
        print (
            'Difficulty =',
            difficulty,
            'Time =',
            timetaken,
            'Nounce =',
            nounce,
            'Hash =',
            sha.hexdigest(),
            )



			