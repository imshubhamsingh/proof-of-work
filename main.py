from datetime import datetime as dt
from pow import proof_of_work

if __name__ == '__main__':
    data = dt.now().strftime("%I:%M%p on %B %d, %Y")
    proof_of_work(data,'0')
    proof_of_work(data,'00')
    proof_of_work(data,'000')
    proof_of_work(data,'0000')
    proof_of_work(data,'00000')

    