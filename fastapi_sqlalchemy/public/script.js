const body = document.body;
const nav = document.querySelector(".page-header nav");
const menu = document.querySelector(".page-header .menu");
const scrollUp = "scroll-up";
const scrollDown = "scroll-down";
let lastScroll = 0;
window.addEventListener("scroll", () => {
  const currentScroll = window.pageYOffset;
  if (currentScroll <= 0) {
    body.classList.remove(scrollUp);
    return;
  }
  if (currentScroll > lastScroll && !body.classList.contains(scrollDown)) {
    // down 
    body.classList.remove(scrollUp);
    body.classList.add(scrollDown);
  } else if (
    currentScroll < lastScroll &&
    body.classList.contains(scrollDown)
  ) {
    // up 
    body.classList.remove(scrollDown);
    body.classList.add(scrollUp);
  }
  lastScroll = currentScroll;
});

















// Отримання всіх користувачів
async function getUsers() {
  // надсилає запит і отримуємо відповідь
  const response = await fetch("/api/users", {
      method: "GET",
      headers: { "Accept": "application/json" }
  });
  // якщо запит пройшов нормально
  if (response.ok === true) {
      // отримуємо дані
      const users = await response.json();
      const rows = document.querySelector("tbody");
      // додаємо отримані елементи в таблицю
      users.forEach(user => rows.append(row(user)));
  }
}



// Отримання одного користувача
async function getUser(id) {
  const response = await fetch(`/api/users/${id}`, {
      method: "GET",
      headers: { "Accept": "application/json" }
  });
  if (response.ok === true) {
      const user = await response.json();
      document.getElementById("userId").value = user.id;
      document.getElementById("userName").value = user.name;
      document.getElementById("userSurname").value = user.surname;
      document.getElementById("userPhone").value = user.phone;
      document.getElementById("userEmail").value = user.email;
      document.getElementById("userStart").value = user.start;
      document.getElementById("userFinish").value = user.finish;
      document.getElementById("userDate").value = user.date;
      document.getElementById("userComment").value = user.comment;
  }
  else {
      // якщо сталася помилка, отримуємо повідомлення про помилку
      const error = await response.json();
      console.log(error.message); // і виводимо його на консоль
  }
}








// Додавання користувача
async function createUser(userName, userSurname, userPhone, userEmail, userStart, userFinish, userDate, userComment) {
 
  const response = await fetch("api/users", {
      method: "POST",
      headers: { "Accept": "application/json", "Content-Type":

      "application/json" },

      body: JSON.stringify({
          name: userName,
          surname: userSurname,
          phone: userPhone,
          email:userEmail,
          start:userStart,
          finish:userFinish,
          date:userDate,
          comment:userComment
      })
  });
  if (response.ok === true) {
      const user = await response.json();
      document.querySelector("tbody").append(row(user));
      reset();
  }
  else {
      const error = await response.json();
      console.log(error.message);
  }
}




// Зміна користувача
async function editUser(userId, userName, userSurname, userPhone, userEmail, userStart, userFinish, userDate, userComment) {
  const response = await fetch("api/users", {
      method: "PUT",
      headers: { "Accept": "application/json", "Content-Type":

      "application/json" },

      body: JSON.stringify({
      id: userId,
      name: userName,
      surname: userSurname,
      phone: userPhone,
      email:userEmail,
      start:userStart,
      finish:userFinish,
      date:userDate,
      comment:userComment
      })
  });
  if (response.ok === true) {
      const user = await response.json();

      document.querySelector(`tr[data-rowid='${user.id}']`).replaceWith(row(user));
      location.reload();

  }
  else {
      const error = await response.json();
      console.log(error.message);
  }
}





// Видалення користувача
async function deleteUser(id) {
  const response = await fetch(`/api/users/${id}`, {
      method: "DELETE",
      headers: { "Accept": "application/json" }
  });
  if (response.ok === true) {
      const user = await response.json();
      document.querySelector(`tr[data-rowid='${user.id}']`).remove();
  }
  else {
      const error = await response.json();
      console.log(error.message);
  }
}




// скидання даних форми після відправлення
function reset() {
  document.getElementById("userId").value =
  document.getElementById("userName").value =
  document.getElementById("userSurname").value =
  document.getElementById("userPhone").value =
  document.getElementById("userEmail").value =
  document.getElementById("userStart").value =
  document.getElementById("userFinish").value =
  document.getElementById("userDate").value =
  document.getElementById("userComment").value =""
}


// створення рядка для таблиці
function row(user) {
  const tr = document.createElement("tr");
  tr.setAttribute("data-rowid", user.id);

  if (window.location.href.includes("/admin")) {
    
    const idTd = document.createElement("td");
    idTd.append(user.id);
    tr.append(idTd);
}

  const nameTd = document.createElement("td");
  nameTd.append(user.name);
  tr.append(nameTd);

  if (window.location.href.includes("/admin")) {

    const surnameTd = document.createElement("td");
    surnameTd.append(user.surname);
    tr.append(surnameTd);

    const phoneTd = document.createElement("td");
    phoneTd.append(user.phone);
    tr.append(phoneTd);

    const emailTd = document.createElement("td");
    emailTd.append(user.email);
    tr.append(emailTd);

}

  const startTd = document.createElement("td");
  startTd.append(user.start);
  tr.append(startTd);

  const finishTd = document.createElement("td");
  finishTd.append(user.finish);
  tr.append(finishTd);

  const dateTd = document.createElement("td");
  dateTd.append(user.date);
  tr.append(dateTd);

  
  const commentTd = document.createElement("td");
  commentTd.append(user.comment);
  tr.append(commentTd);
  

  if (window.location.href.includes("/admin")){
    const linksTd = document.createElement("td");
    linksTd.classList.add("table__buttons"); 

    const editLink = document.createElement("button");
    editLink.append("Змінити");
    editLink.classList.add("table__change");
    editLink.addEventListener("click", async() => await getUser(user.id));
    linksTd.append(editLink);

    const removeLink = document.createElement("button");
    removeLink.append("Видалити");
    removeLink.classList.add("table__remove");
    removeLink.addEventListener("click", async () => await deleteUser(user.id));

    linksTd.append(removeLink);
    tr.appendChild(linksTd);
  }
  return tr;
}


// скидання значень форми
document.getElementById("resetBtn").addEventListener("click", () => reset());


// надсилання форми
document.getElementById("saveBtn").addEventListener("click", async () => {
  const id = document.getElementById("userId").value;
  const name = document.getElementById("userName").value;
  const surname = document.getElementById("userSurname").value;
  const phone = document.getElementById("userPhone").value;
  const email = document.getElementById("userEmail").value;
  const start = document.getElementById("userStart").value;
  const finish = document.getElementById("userFinish").value;
  const date = document.getElementById("userDate").value;
  const comment = document.getElementById("userComment").value;
  if (id === "")
      await createUser(name, surname, phone, email, start, finish, date, comment);
  else
      await editUser(id, name, surname, phone, email, start, finish, date, comment);
  reset();
});


// завантаження користувачів
getUsers();


