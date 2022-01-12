    function getUsers(id){
    console.log('clicked')
        link= 'https://reqres.in/api/users/' + id
         console.log(link)
    fetch(link).then(
    response => response.json()
    ).then(
        response_object => put_users_inside_html(response_object.data)
    ).catch(
        err=> console.log(err)
    )
}

function  put_users_inside_html(response_obj_data){
       console.log(response_obj_data);
    const curr_main = document.querySelector("body");
    user = response_obj_data
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
    curr_main.appendChild(section)


}