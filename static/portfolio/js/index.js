 // scroll effect
        
const divs = document.querySelectorAll("div");
    
window.addEventListener('scroll',checkBoxs);

checkBoxs();

function checkBoxs(){
    const triggerBottom = window.innerHeight/4*4;

    divs.forEach((div) =>{
        const boxTop = div.getBoundingClientRect().top;

        if(boxTop < triggerBottom){
            div.classList.add('show');
        }else{
            div.classList.remove('show');
        }
    });
};


  // form submission

// form.addEventListener('submit', function(e) {
// const formData = new FormData(form);
// e.preventDefault();

// const object = Object.fromEntries(formData);
// const json = JSON.stringify(object);

// result.innerHTML = "Please wait..."

// fetch('https://api.web3forms.com/submit', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'Accept': 'application/json'
//         },
//         body: json
//     })
//     .then(async (response) => {
//     let json = await response.json();
//     if (response.status == 200) {
//         result.innerHTML = json.message;
//         result.classList.remove("text-gray-500");
//         result.classList.add("text-green-500");
//     } else {
//         console.log(response);
//         result.innerHTML = json.message;
//         result.classList.remove("text-gray-500");
//         result.classList.add("text-red-500");
//     }
//     })
});

// mobile menu

// const mobileIcon = document.querySelector("#bugger");
// const menu = document.querySelector("#menu");

// mobileIcon.addEventListener("click",()=>{
//     menu.classList.toggle("hidden");
// });

const humbugger = document.querySelector(".fa-solid");
const menu = document.querySelector("#menu");
const link = document.querySelector("#hlink");

const faSolid = document.querySelector(".fa-solid");

humbugger.addEventListener('click',()=>{
    menu.classList.toggle("hidden");
    humbugger.classList.toggle("fa-xmark");
});
