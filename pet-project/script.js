// варианты

let checkboxStates = {
  name: false,
  lastname: false,
  age: false,
  phone_number: false,
  city: false,
};

function handleCheckboxChange(event) {
  const checkboxName = event.target.name;
  checkboxStates[checkboxName] = event.target.checked;
  console.log(checkboxStates);
}

document
  .querySelectorAll(".name, .lastname, .age, .phone_number, .city")
  .forEach(function (element) {
    element.addEventListener("change", handleCheckboxChange);
  });

// язык

let radioStates = {
  name_lastname_ru: "",
  name_lastname_en: "",
  number_city_ru: "",
  number_city_en: "",
};

function handleRadioChange(event) {
  const radioName = event.target.id;
  const radioValue = event.target.value;

  if (event.target.checked) {
    radioStates[radioName] = radioValue;
  } else {
    radioStates[radioName] = "";
  }

  document
    .querySelectorAll(`input[type='radio'][name='${event.target.name}']`)
    .forEach((radio) => {
      if (radio !== event.target) {
        radio.checked = false;
        radioStates[radio.id] = "";
      }
    });

  console.log(radioStates);
}

document.querySelectorAll("input[type='radio']").forEach(function (radio) {
  radio.addEventListener("change", handleRadioChange);
});

// возраст
const submitBtn = document.querySelector(".submit_age");
const ageFromInput = document.getElementById("age_from");
const ageTillInput = document.getElementById("age_till");

function handleInputChange() {
  const ageFromValue = ageFromInput.value;
  const ageTillValue = ageTillInput.value;
  console.log("От:", ageFromValue, "До:", ageTillValue);
}
ageFromInput.addEventListener("input", handleInputChange);
ageTillInput.addEventListener("input", handleInputChange);
submitBtn.addEventListener("click", handleInputChange);

document
  .getElementById("age_form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
  });
