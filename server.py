from flask import Flask,redirect
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# Data

freekicks = {
    "1": {
        "id": "1",
        "name": "Curved",
        "description": "Spin on the ball makes the ball move in a curved direction.",
        "execution": "Hit the ball with your instep to generate the curl.",
        "goal": "Curl the ball over or around the wall of defending players, out of the reach of the goalkeeper.",
        "video": "https://www.youtube.com/embed/vR2Grj1f0VE?start=0&end=3&mute=1",
        "prev_page": 1,
        "next_page": 2
    },
    "2": {
        "id": "2",
        "name": "Knuckleball",
        "description": "Ball kicked at very low spin, which results in a zigzag trajectory.",
        "execution": "Hit the middle of the ball with the laces of your shoe.",
        "goal": "Make the ball suddenly change directions so that the goalkeeper cannot predict its trajectory.",
        "video": "https://www.youtube.com/embed/JQYBM0p-j6I?start=0&end=4&mute=1",
        "prev_page": 1,
        "next_page": 3
    },
    "3": {
        "id": "3",
        "name": "Under the Wall",
        "description": "When the ball is hit with power into the space left by the jumping wall of defending players.",
        "execution": "Pretend that you will fire a high kick but when the opponents jump send the ball under them.",
        "goal": "To catch the goalkeeper off-guard as he is expecting the ball to come over the wall.",
        "video": "https://www.youtube.com/embed/Le7djCa7oCY?start=0&end=9&mute=1",
        "prev_page": 2,
        "next_page": 4
    },
    "4": {
        "id": "4",
        "name": "Cross",
        "description": "Bringing the ball into the opponent box with a medium-to-long range pass.",
        "execution": "Chip the ball over defenders by slicing it from the bottom with your insole.",
        "goal": "Get the ball out of the reach of defenders into the opponent box to create a goal scoring chance.",
        "video": "https://www.youtube.com/embed/WJIa3AUle_g?start=135&end=140&mute=1",
        "end": "6",
        "prev_page": 3,
        "next_page": 5
    },
    "5": {
        "id": "5",
        "name": "Team Routine",
        "description": "Bringing the ball into the opponent box with a short-to-medium range pass.",
        "execution": "Pass the ball to a closer teammate who has a better clearing from defenders.",
        "goal": "Get the ball into opponent box by passing to least defended attacking forward to either score or create a better scoring chance.",
        "video": "https://www.youtube.com/embed/B39Y8UvOitI?start=4&end=12&mute=1",
        "end": "12",
        "prev_page": 4,
        "next_page": 5
    },
}

quiz_data = {
    "1": {
        "id": "1",
        "title": "Question 1",
        "data_type": "video",
        "data": "https://www.youtube.com/embed/ZAqifjaXRXE?start=0&end=6&mute=1",
        "question": "Play the video and identify the type of Free Kick that was used.",
        "answer1": "Curved",
        "answer2": "Knuckleball",
        "answer3": "Cross",
        "answer4": "Team Routine",
        "correct_answer": 2,
        "prev_page": 1,
        "next_page": 2,
        "explanation": "You seem to not have been able to identify a knuckleball free kick.",
        "explanation_link": "/freekick/2",
    },
    "2": {
        "id": "2",
        "title": "Question 2",
        "data_type": "text",
        "data": "Ball kicked at very low spin, which results in a zigzag trajectory...",
        "question": "Hey, next David Beckham!  Which type of free kick fits the description above?",
        "answer1": "Curved",
        "answer2": "Knuckleball",
        "answer3": "Cross",
        "answer4": "Team Routine",
        "correct_answer": 2,
        "prev_page": 1,
        "next_page": 3,
        "explanation": "To get the ball moving in a zigzag trajectory, you've got to kick it with your instep and that is a knuckleball freekick.",
        "explanation_link": "/freekick/2",
    },
    "3": {
        "id": "3",
        "title": "Question 3",
        "data_type": "video",
        "data": "https://www.youtube.com/embed/LeaV-gfLz5U?start=7&end=15&mute=1",
        "end": "16",
        "question": "What type of free kick did Messi execute and with which part of the foot did he use?",
        "answer1": "Curved, In-step",
        "answer2": "Knuckleball, Laces",
        "answer3": "Curved, Laces",
        "answer4": "Knuckleball, In-step",
        "correct_answer": 1,
        "prev_page": 2,
        "next_page": 4,
        "explanation": "From the video, Messi kicked with ball with his instep. That can only result in a curved trajectory!",
        "explanation_link": "/freekick/1",
    },
    "4": {
        "id": "4",
        "title": "Question 4",
        "data_type": "picture",
        "data": "/static/images/4.png",
        "alt": "Pep Guardiola with speech bubble saying 'The wall always jumps very high.'",
        "question": "How do you kick the ball if Pep Guardiola, the smartest manager, gives you the advice above? ",
        "answer1": "Curved",
        "answer2": "Knuckleball",
        "answer3": "Under The Wall",
        "answer4": "Team Routine",
        "correct_answer": 3,
        "prev_page": 3,
        "next_page": 5,
        "explanation": "If the wall jumps high, then there will always be a space beneath the wall! You would want to kick the ball under the wall then.",
        "explanation_link": "/freekick/3",
    },
    "5": {
        "id": "5",
        "title": "Question 5",
        "data_type": "picture",
        "data": "https://library.sportingnews.com/2021-08/wanderers-free-kick_vpvg34l3y7jc14m3yhegoi05l.jpg",
        "alt": "A row of players lined up directly in front of the goal, blocking it",
        "question": "From the picture above, what would be the best free kick that would likely result in a goal?",
        "answer1": "Curved because the ball must be out of the reach of the goalkeeper",
        "answer2": "Knuckleball because you want to change the direction of the ball",
        "answer3": "Cross because you want the ball over the defenders",
        "answer4": "Team Routine because there is a least guarded teammate close to you.",
        "correct_answer": 4,
        "prev_page": 4,
        "next_page": 5,
        "explanation": "Well you could score on your own, but passing to your nearby teammate creates the best chance.",
        "explanation_link": "/freekick/5",
    }
}

quiz_score = 0 
correct_answered_questions = []
wrong_answered_questions = []


# ROUTES
@app.route('/')
def welcome():
    return render_template('home_page.html', data=freekicks)

@app.route('/freekick/<id>')
def freekick(id):
    return render_template('freekick.html', freekick=freekicks[id])

@app.route('/quiz_home')
def quiz_home():
    global quiz_score
    global correct_answered_questions
    global wrong_answered_questions
    quiz_score = 0

    correct_answered_questions = []
    wrong_answered_questions = []

    return render_template('quiz_home.html')

@app.route('/quiz/<id>')
def quiz_generate_ques(id):
    return render_template('quiz.html', data=quiz_data[id])

@app.route('/quiz/quiz_feedback',methods=["GET","POST"])
def quiz_evaluate_ans():
    global quiz_score
    global quiz_data
    global correct_answered_questions
    global wrong_answered_questions

    json_data = request.get_json()

    question_no = json_data['question_number']
    answer_selected = json_data['answer_number']

    question = quiz_data[question_no]


    if str(question["correct_answer"])== str(answer_selected):
        quiz_score=quiz_score+1
        correct_answered_questions.append(question_no)
    else:
        wrong_answered_questions.append(question_no)
    
    next_id = int(question_no) + 1

    if next_id > 5:
        end_state = {"id": 6}
        return jsonify(data=end_state)


    return jsonify(data=quiz_data[str(next_id)])

@app.route('/quiz/end')
def quiz_end():
    global quiz_score
    global correct_answered_questions
    global wrong_answered_questions
    global quiz_data

    num_correct = correct_answered_questions
    num_wrong = wrong_answered_questions

    wrong_feedback = {}

    for i in num_wrong:
        temp = {}
        temp["id"] = i
        temp["explanation"] = quiz_data[i]["explanation"]
        temp["explanation_link"] = quiz_data[i]["explanation_link"]
        wrong_feedback[i]=temp

    print(wrong_feedback)
    return render_template('quiz_end.html', score = quiz_score, wrong_feedback=wrong_feedback, wrong = num_wrong)  


if __name__ == '__main__':
    app.run(debug = True)




