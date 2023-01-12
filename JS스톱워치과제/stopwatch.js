let minutes=0;
let seconds=0;
let ten_milis=0;
let intervalId;

const appendMinutes=document.getElementById('minutes');
const appendSeconds=document.getElementById('seconds');
const appendTenMilis=document.getElementById('ten_milis');

const buttonStart=document.getElementById('bt_start');
const buttonStop=document.getElementById('bt_stop')
const buttonReset=document.getElementById('bt_reset');

const button_delete=document.querySelector('#delete');
const button_checkAll=document.querySelector('#checkAll');


buttonStart.onclick=function(){
    clearInterval(intervalId);
    intervalId=setInterval(operateTimer,10)
}

buttonStart.onclick=()=>{
    clearInterval(intervalId);
    intervalId=setInterval(operate)
}

buttonStop.onclick=()=>{
    clearInterval(intervalId);//저 id를 가진 inerval이 동작 멈추기
    addTime();
}

buttonReset.onclick=()=>{
    clearInterval(intervalId);
    ten_milis=0;
    seconds=0;
    minutes=0;

    appendMinutes.innerText="00";
    appendSeconds.innerText="00";
    appendTenMilis.innerText="00";

}

button_delete.onclick=()=>{
    deleteSelected();
}

button_checkAll.onclick=()=>{
    checkAll();
}



function operateTimer(){
    ten_milis++;
    appendTenMilis.textContent=String(ten_milis).padStart(2,0);

    if(ten_milis>99){
        seconds++;
        appendSeconds.textContent=String(seconds).padStart(2,0);
        ten_milis=0;
        appendTenMilis="00";
    }

    if(seconds>59){
        minutes++;
        appendMinutes.textContent=String(minutes).padStart(2,0);
        seconds=0;
        appendSeconds.textContent="00";
    }
}

function addTime(){
    var tr=document.createElement("tr");
    var input=document.createElement("input");

    input.setAttribute("type","checkbox");
    input.setAttribute("class","checkcheck");

    var td01=document.createElement("td");
    td01.appendChild(input);

    var td02=document.createElement("td");
    td02.innerHTML=String(minutes).padStart(2,0)+":"+String(seconds).padStart(2,0)+":"+String(ten_milis).padStart(2,0);

    tr.appendChild(td01);
    tr.appendChild(td02);

    document.querySelector('#listbody').appendChild(tr);
    //document.getElementById("listbody").appendChild(tr);

}

function checkAll(){
   // var list=document.getElementById('listbody');

    //var listChild=list.children;
    //for(var i=0;i<listChild.length;i++){
       // list.removeChild(listChild[i]);
    //}

    
        var checkboxs=document.querySelectorAll('#listbody .checkcheck');
        if(button_checkAll.checked){
            for (var i in checkboxs){
                checkboxs[i].checked=true; 
            }
        }
        else{
            for (var i in checkboxs){
                checkboxs[i].checked=false; 
            }

        }
   
}

function deleteSelected(){
    var list=document.getElementById('listbody');
    var checkbox=document.querySelectorAll('#listbody .checkcheck');

    for (var i in checkbox){
        if(checkbox[i].checked) list.removeChild(checkbox[i].parentNode.parentNode);
    }

}