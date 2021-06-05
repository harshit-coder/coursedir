var quiz1 = [...document.getElementsByClassName('quiz')]
const url = window.location.href
quiz1.forEach(qu => qu.addEventListener('click', () => {


    var quest = qu.getAttribute('data-quest')
    var time = qu.getAttribute('data-time')
    var pk = qu.getAttribute('data-pk')

    window.location.href = url + "start_quiz/" + pk

}))