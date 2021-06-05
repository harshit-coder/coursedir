console.log("hello world quiz1")
const quizform = document.getElementById('quizform')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const timerbox = document.getElementById('timerbox')
const url1 = window.location.href

const activatetimer = (time) => {
    console.log(time)
    if (time.toString().length < 2) {
        timerbox.innerHTML = '<li class="minutes"><span class="count-down-number">0' + time + '</span><span class="count-unit">Min</span></li><li class="seconds"><span class="count-down-number">:00</span><span class="count-unit">Sec</span></li>'
    } else {
        timerbox.innerHTML = '<li class="minutes"><span class="count-down-number">' + time + '</span><span class="count-unit">Min</span></li><li class="seconds"><span class="count-down-number">:00</span><span class="count-unit">Sec</span></li>'
    }
    let min = time - 1
    let sec = 60
    let dismin
    let dissec
    const timer = setInterval(() => {
        sec = sec - 1
        if (sec < 0) {
            sec = 59
            min = min - 1
        }
        if (min.toString().length < 2) {
            dismin = '0' + min

        } else {
            dismin = min
        }
        if (sec.toString().length < 2) {
            dissec = '0' + sec

        } else {
            dissec = sec
        }

        if (min === 0 && sec === 0) {
            timerbox.innerHTML = '<b>00:00</b>'
            setTimeout(() => {
                clearInterval(timer)
                alert('Time is over')
                senddata()
            }, 500)
            console.log('timeover')
        }
        timerbox.innerHTML = '<li class="minutes"><span class="count-down-number">' + dismin + '</span><span class="count-unit">Min</span></li><li class="seconds"><span class="count-down-number">:' + dissec + '</span><span class="count-unit">Sec</span></li>'
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: url1 + 'quiz',
    success: function(response) {
        console.log(response)
        const data = response.data
        var i = 1
        const da = data.length
        data.forEach(el => {
            if (i === 1) {
                for (const [quest, answer] of Object.entries(el)) {
                    out1 = '  <div class="quiz-title text-center"><span>Question'+ i +'</span><p>' + quest + '</p></div>'
                    out2 = out1 + '<div class="quiz-option-selector clearfix"><ul>'
                    answer.forEach(ans => {
                        out2 += '<li><label class="start-quiz-item"><input type="radio" id="' + quest + '-' + ans + '" name="' + quest + '" value="' + ans + '" class="exp-option-box"><span class="exp-label">' + ans + '</span><span class="checkmark-border"></span></label></li>'
                    })
                    out2 += '</ul></div>'
                    quizbox.innerHTML += out2
                }
            } else if (i === da) {
                for (const [quest, answer] of Object.entries(el)) {
                    out1 = '  <div class="quiz-title text-center"><span>Question'+ i +'</span><p>' + quest + '</p></div>'
                    out2 = out1 + '<div class="quiz-option-selector clearfix"><ul>'
                    answer.forEach(ans => {
                        out2 += '<li><label class="start-quiz-item"><input type="radio" id="' + quest + '-' + ans + '" name="' + quest + '" value="' + ans + '" class="exp-option-box "><span class="exp-label">' + ans + '</span><span class="checkmark-border"></span></label></li>'
                    })
                    out2 += '</ul></div>'
                    quizbox.innerHTML += out2
                }

            } else {
                for (const [quest, answer] of Object.entries(el)) {
                    out1 = '  <div class="quiz-title text-center"><span>Question'+ i +'</span><p>' + quest + '</p></div>'
                    out2 = out1 + '<div class="quiz-option-selector clearfix"><ul>'
                    answer.forEach(ans => {
                        out2 += '<li><label class="start-quiz-item"><input type="radio" id="' + quest + '-' + ans + '" name="' + quest + '" value="' + ans + '" class="exp-option-box "><span class="exp-label">' + ans + '</span><span class="checkmark-border"></span></label></li>'
                    })
                    out2 += '</ul></div>'
                    quizbox.innerHTML += out2
                }
            }
            i = i + 1
        });

        quizbox.innerHTML+= '<div class="actions clearfix" style="text-align:center;"><div><button class="js-btn-submit" style="background-color: red;width: 201px;height: 44px;color: white;font-weight: bold;font-size: x-large;font-family: -webkit-body;" type="submit"><span>SUBMIT</span></button></div></div>'
        activatetimer(response.time)
    },
    error: function(error) {},
})


const senddata = () => {
    var el = [...document.getElementsByClassName('exp-option-box')]

    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    el.forEach(e => {
        if (e.checked) {

            data[e.name] = e.value
        } else {
            if (!data[e.name]) {
                data[e.name] = null
            }
        }

    })

    $.ajax({

        type: 'POST',
        url: url1 + "save/",

        data: data,
        success: function(response) {
            console.log(response.score)

            window.location.href = url1 + response.score +"/result"

        },

        error: function(error) {
            console.log(error)
        }


    })



}

quizform.addEventListener('submit', e => {
    e.preventDefault()
    senddata()
})


