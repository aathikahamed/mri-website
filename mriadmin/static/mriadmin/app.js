sent = document.querySelector("#sent-success");
sent.style.display = "none";
document.querySelector("#contact-form").onsubmit = () => {
  let firstname = document.querySelector("#first_name");
  let lastname = document.querySelector("#last_name");
  let email = document.querySelector("#email");
  let phone = document.querySelector("#phone_number");
  let subject = document.querySelector("#subject");
  let message = document.querySelector("#message");
  let check = document.querySelector("#check").value;
  if (check === "") {
    fetch("/contact_api/", {
      method: "POST",
      body: JSON.stringify({
        firstname: firstname.value,
        lastname: lastname.value,
        email: email.value,
        phone: phone.value,
        subject: subject.value,
        message: message.value,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        firstname.value = "";
        lastname.value = "";
        email.value = "";
        phone.value = "";
        subject.value = "";
        message.value = "";
        sent.style.display = "block";
      });
  } else {
    //   Checking for hackers
    console.log("invalid");
  }
  return false;
};
