// login/Sign up functionality

let signup = document.querySelector(".login-signup");
let login = document.querySelector(".login-login");
let slider = document.querySelector(".login-slider");
let formSection = document.querySelector(".login-form-section");

signup.addEventListener("click", () => {
    slider.classList.add("login-moveslider");
    formSection.classList.add("login-form-section-move");
});

login.addEventListener("click", () => {
    slider.classList.remove("login-moveslider");
    formSection.classList.remove("login-form-section-move");
});

// Username validation

document.getElementById('username').addEventListener('input', function() {
    var usernameInput = document.getElementById('username');
    var errorMessage = document.getElementById('username-error');
    var existingUsernames = ['up1', 'up2', 'up3']; // Static list for demonstration

    if (existingUsernames.includes(usernameInput.value.trim())) {
        errorMessage.textContent = 'Username already taken';
        errorMessage.classList.add('active');
    } else {
        errorMessage.textContent = '';
        errorMessage.classList.remove('active');
    }
});

// Password matching validation

document.getElementById('ConfirmPassword').addEventListener('input', function() {
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.getElementById('ConfirmPassword');
    var errorMessage = document.getElementById('password-match-error');

    if (passwordInput.value === confirmPasswordInput.value) {
        errorMessage.textContent = 'Passwords match';
        errorMessage.classList.remove('no-match');
        errorMessage.classList.add('match');
    } else {
        errorMessage.textContent = 'Passwords do not match';
        errorMessage.classList.remove('match');
        errorMessage.classList.add('no-match');
    }
});

// Toggle password visibility

function togglePassword(fieldId, icon) {
    var passwordField = document.getElementById(fieldId);
    var passwordFieldType = passwordField.getAttribute('type');

    if (passwordFieldType === 'password') {
        passwordField.setAttribute('type', 'text');
        icon.classList.remove('bx-hide');
        icon.classList.add('bx-show');
    } else {
        passwordField.setAttribute('type', 'password');
        icon.classList.remove('bx-show');
        icon.classList.add('bx-hide');
    }
}

//Toast

let toastBox = document.getElementById('toastBox');
let loginmsg = '<i class="fa-solid fa-square-check"></i>Successfully logged in.';
let signupmsg = '<i class="fa-solid fa-square-xmark"></i>Account created successfully.';

function showToast(msg) {
    let toast = document.createElement('div');
    toast.classList.add('toast');
    toast.innerHTML = msg;
    toastBox.appendChild(toast);

    if(msg.includes('successfully')){
        toast.classList.add('error');
    }

    setTimeout(()=>{
        toast.remove();
    },5000);
}


// channels

function openModal(modalId) {
    document.getElementById(modalId).style.display = "flex";
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none";
}

//faqs

function toggleFaq(element) {
    const faq = element.parentElement;
    faq.classList.toggle("open");
}