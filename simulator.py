import random
from time import sleep
import faker

fake = faker.Faker()

number_of_humans_to_generate = 6
humans = []
total_baby_born = []

members = ['friends','family','coworkers','girlfriend','boyfriend']
jobs = ['software enginer','developer','assistant','product designer','cook','maid','babysitter','IT Engineer','architect','marketer']
doing_other_thing = ['watching television','playing with kids','having sex','eating dinner','sleeping','playing video game','masturbating']
going_outside = ['beach','park','mall','restaurant','bar','cafe','movie theater','gym','school','home','club']
random_incidents = ['got crashed with a car','robbed','killed by a zombie','on his way and got caught by his boss','caught by the police for over speeding','killed by a serail killer']

humans_who_took_leave = []
job_done = False
human_had_a_baby = False
amount_of_time_to_rest = random.randint(1,4)


def create_human(human):
    humans.append(human)


def baby_life(human):
    sleep(amount_of_time_to_rest)
    print(f'{human} is now {random.randint(1,8)} years old')
    sleep(amount_of_time_to_rest)
    print(f'{human} is now {random.randint(10,20)} years old')
    sleep(amount_of_time_to_rest)
    print(f'{human} is now capable of doing job')
    print(f'I hope you succed in life 👏 {human}')
    sleep(amount_of_time_to_rest)

    create_human(human)


def do_job(human):
    job = random.choice(jobs)
    job_time = random.randint(2,9)

    print(f'\n{human} is a {job} and is working for {job_time} hours')


def go_to_home(human):
    print(f'{human} is going home')
    sleep(amount_of_time_to_rest)

    other_thing = random.choice(doing_other_thing)
    # other_thing = 'having sex'

    if 'sex' in other_thing:
        if random.randint(1,2) == 1:
            print(f'{human} reached home and {other_thing}\n')

            baby_name = fake.first_name()
            total_baby_born.append(baby_name)
            human_had_a_baby = True

            sleep(amount_of_time_to_rest)
            print(human, 'had a baby', baby_name)
            print(f'Congrats on your baby 🎉')
            sleep(amount_of_time_to_rest)

            print(f'{baby_name} will now continue for his baby life')
            
            sleep(amount_of_time_to_rest)
            baby_life(baby_name)
        else:
            human_had_a_baby = False
            print(f'{human} reached home and {other_thing} with protection\n')

    else:
        print(f'{human} reached home and {other_thing}\n')



def go_outside(human):
    random_incident = random.randint(1,2)
    random_saves = ['ambulance','police','local people','girlfriend','boyfriend','sister','father','random guy']
    
    print(f'{human} is going outside')
    sleep(amount_of_time_to_rest)

    if random_incident == 1:
        incident_occured = random.choice(random_incidents)
        
        if 'killed' in incident_occured:
            print(f'{human} was {incident_occured} RIP 🪦')

        elif 'robbed' in incident_occured:
            print(f'{human} was {incident_occured} and has no money left 💰')

        elif 'crashed' in incident_occured:
            print(f'{human} {incident_occured} 🚘')
            sleep(amount_of_time_to_rest)

            random_saved = random.choice(random_saves)
            if random.randint(1,2) == 1:
                print(f'{human} was rescued by a {random_saved}')
            else:
                print(f'{human} is dead {random_saved} were late to save him 💀')

        elif 'police' in incident_occured:
            print(f'{human} was {incident_occured} 🚓')
        else:
            print(f'{human} was {incident_occured}')

    elif random_incident == 2:
        print(f'{human} reached {random.choice(going_outside)} with his {random.choice(members)}')



def simulate():
    for human in humans:
        took_a_leave = [True,False]

        if random.choice(took_a_leave) == True:
            humans_who_took_leave.append(human)
            job_done = False
            print(f'\n{human} took a leave')
        else:
            do_job(human)
            sleep(amount_of_time_to_rest)
            job_done = True

        if job_done:
            random_place = random.randint(1,2)
            if random_place == 1:
                go_to_home(human)
            elif random_place == 2:
                go_outside(human)
                # go_to_home(human)

        else:
            continue
    

    print('\nAll jobs done!')
    print(f'Total Humans: {len(humans)}')   
    print(f'Total Babies Born: {len(total_baby_born)}')
    print(f'{len(humans_who_took_leave)} Humans took a leave today \n')

    
for _ in range(1,number_of_humans_to_generate):
    human = fake.first_name()
    create_human(human)

simulate()