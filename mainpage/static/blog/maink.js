let name0 = document.getElementById("id_name"),
    subject0 = document.getElementById("id_subject"),
    email = document.getElementById("id_email"),
    body = document.getElementById("id_body"),
    porgress_bar = document.getElementsByClassName("progress-bar"),
    pro1 = document.getElementsByClassName("pro1"),
    proar = document.getElementById("progress_area");

let run = 0;
console.log(run);

console.log(run);
proar.addEventListener('mouseenter', function(e){
    if (run == 0){
    for (let p = 0; p < porgress_bar.length; p++){
        console.log(p);
        console.log(porgress_bar[p].style.width);
        let i = 1;
        function frame(){
            if (i == pro1[p].innerHTML){
                clearInterval(id);
                stop();
            }
            porgress_bar[p].style.width = i+"%";
            i++;
        }
        let id = setInterval(frame, 10);
    }
    run = 1;
}
})



subject0.classList.add("form-control");
subject0.classList.add("input-mf");
email.setAttribute("class", "form-control input-mf");
name0.setAttribute("class", "form-control input-mf");
body.setAttribute("class", "form-control input-mf");
name0.setAttribute("placeholder", "Name *");
email.setAttribute("placeholder", "Email *");   

