from flask import Flask, render_template
from data import db_session
from data.user import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()
    request = session.query(Jobs).all()
    param = {}
    param['title'] = 'Домашняя страница'
    param['jobs'] = create_jobs_dict(request)
    return render_template('tables.html', **param)

def create_jobs_dict(jobs_list):
    jobs_dict = {}
    for elem in jobs_list:
        jobs_dict[elem.id] = [{
            'job_description': elem.job,
            'team_leader': elem.team_leader_instance,
            'work_size': elem.work_size,
            'collaborators': elem.collaborators,
            'is_finished': elem.is_finished,

        }]
    print(jobs_dict)
    return jobs_dict

def user_create(surname, name, age, position, speciality, address, email, hashed_password):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.hashed_password = hashed_password
    return user

def job_create(team_leader, description, work_size, collaborators, is_finished):
    job = Jobs()
    job.team_leader = team_leader
    job.job = description
    job.work_size = work_size
    job.collaborators = collaborators
    job.is_finished = is_finished
    print(job)
    return job

def main():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    '''try:

        db_sess.add(user_create("Scott", "Ridley", 21, "captain",
                                "research engineer", "module_1", "scott_chief@mars.org", "cap"))
        db_sess.commit()
        db_sess.add(user_create("Kushnarev", "Aleksey", 16, "student",
                                "programmer", "module_2", "Aleksey@mars.org", "notcap"))
        db_sess.commit()
        db_sess.add(user_create("Popov", "Arthur", 17, "DJ",
                                "dj", "module_1", "Arthur@mars.org", "dj"))
    except(Exception):
        print('данные уже есть в таблице')

    try:
        db_sess.add(job_create(1, 'deployment of residential modules 1 and 2', 15, '2, 3', False))
        db_sess.commit()
    except(Exception):
        print('данные уже есть в таблице')

    db_sess.add(Jobs(team_leader=3, job='start/stop music', work_size=25, collaborators='', is_finished=False))
    db_sess.commit()
    try:
        pass
    except(Exception):
        print('данные уже есть в таблице')'''

    db_sess.close()
    app.run(port=8080, host='127.0.0.1')





if __name__ == '__main__':
    main()