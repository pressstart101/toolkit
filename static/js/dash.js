let arr = [];
window.setInterval(function(){
    
    $.get('/api/ping.json', (data) => {
        // alert(JSON.stringify(data));



        if(data){
            let len = data.length;
            let txt = "";
            let cur_val = ""
            

            if(len > 0){
                for(let i=0;i<len;i++){
                    if(data[i].time && data[i].source_ip){
                        txt = "<tr><td>"+data[i].time+"</td><td>"+data[i].source_ip+"</td></tr>";
                        cur_val = {"time":data[i].time, "ip":data[i].source_ip}
                        
                    }
                }
                if(txt != ""){
                    arr.push(cur_val)
                    let latest = arr.slice(Math.max(arr.length - 5, 0));
                    // let str = [];
                    // for(key in latest) {
                    //     if (latest.hasOwnProperty(key)) {
                    //       str.push("Key is " + key + ", value is " + latest[key] + "\n");
                    //     }
                    //   }
                    txt = ""
                    for(let i=0;i<latest.length;i++){
                        txt += `<tr><td>${latest[i].time}</td><td>${latest[i].ip}</td></tr>`
                        // $("#table_body").append(`<tr><td>${latest[i].time}</td><td>${latest[i].ip}</td></tr>`);
                    }
                    $("#table_body").html(txt);
                      
                    // console.log(JSON.stringify(latest));
                    // let str = "<tr><th></th></tr>"
                    // $("#table_body").html(JSON.stringify(latest)); 
                    //#use slice function
                    // $("#table").append(txt);
                    
                    
                }
            }
            let latest = arr.slice(Math.max(arr.length - 5, 0))
            // console.log(arr.slice(Math.max(arr.length - 5, 0)))
            
        }





        // $('#ping').text(JSON.stringify(data));
    });
}, 1000);


// const formValues = $('#xss').serialize();
// $.post("/api/xss.json", formValues, resultHandler);

// $("#url_form").submit(function(e) {

//     e.preventDefault(); // avoid to execute the actual submit of the form.

//     var form = $(this);
//     var url = form.attr('action');
    
//     $.ajax({
//            type: "POST",
//            url: '/api/xss.json',
//            data: form.serialize(), // serializes the form's elements.
//            success: function(data)
//            {
//                alert(data); // show response from the php script.
//            }
//          });

    
// });


function displayResult(data) {
    // alert(data.exploit)
    // let txt = data.exploit
    $('#pageloader').hide()

    let txt = ''
    console.log('\n\n\n DATA from displayresult')
    console.log(data)
    console.log(data.is_vulnerable == false)
    
    // let len = Object.keys(data).length;
    // for(let i=0;i<len;i++){


        // for (let element in data) {
        //     console.log(`${element}: ${data[element]}`)
        //     txt = `${element}: ${data[element]}`;
        //     $("#1").html("").append($("")).text(txt);
        // }
        console.log(`DATA BEFORE IF STATEMENT ${data} \n\n`)
    if (data.is_vulnerable === false) {
        console.log("NOT VULNERABLE from conditional \n\n")
        // $('#table').hide()
        $('#notvuln').show()
        // let not_vuln = document.createElement("h3");
        // not_vuln.innerHTML = "Not Vunrerable to XSS"
        // let xss = document.getElementById('xss')
        // xss.appendChild(not_vuln);
        // $('#xss')
    } else {
        $('#table').show()
        $("#is_vulnerable").text(data.is_vulnerable);
        $("#vuln_url").text(data.url);
        $("#exploit").text(data.exploit);
        $("#vuln_field").text(data.field_name);
        $("#vuln_form_type").text(data.form_type);
        $("#method").text(data.method);

    }
    
    // if (!data.is_vulnerable) {
        // let row = document.createElement("tr");
        // row.innerHTML = `<th>Vulnerable Field Name Tag</th><td id=\'field_name\'>${data.field_name}</td>`

        // let table = document.getElementById("table")
        // table.tBodies[0].appendChild(row);
        // $('table').hide()



        // row.innerHTML = `<th>Successful Exploit </th><td id=\'field_name\'>${data.exploit}</td>`
        // table.tBodies[0].appendChild(row);


    // }


    // data.num_of_vulnerable_forms
    // data.is_vulrerable = True
    // data.field_name
    // data.form_type
    // data.method



        // txt += `${data[i]}`;
        // $("#table_body").append(`<tr><td>${latest[i].time}</td><td>${latest[i].ip}</td></tr>`);
        // console.log(txt)
    // }
    // $("#xss").html("").append($("")).text(txt);
    // $("#1").html("").append($("")).text(txt);
    // $("#2").html("").append($("")).text(txt);


    // $.each(data, function(key, element) {
    //     txt = `${key} ${element}`;
    //     $('#xss')
    //     .html("")
    //     .append($("<td></td>").text(txt))

    // $.each(data, function(key, element) {

                
    //     txt += `<tr><td>${key} ${element} `;
    //     alert(txt);
    //     $("#xss").html(txt);


    // });

    




    // $("#xss").text(data.exploit).val();
    // $("#xss").text(data.url).val();
    // $("#xss").text($(data.exploit).val());

    // data.url
    // data.num_of_vulnerable_forms
    // data.is_vulrerable = True
    // data.field_name
    // data.form_type
    // data.method
    


};



$('#url_form').on('submit', (evt) => {
    evt.preventDefault();
    $('#table').hide()
    $('#notvuln').hide()
    let params = {'url_form': $('#url').val()};

    $.get('/api/xss.json', params, displayResult);
    $('#pageloader').show();

    // let table = $('#table').DataTable();
    // table.ajax.reload();

  });




//   $('#save_report').on('submit', (evt) => {
//     evt.preventDefault();
//     $('#table').hide()
//     $('#notvuln').hide()
//     let params = {'url_form': $('#url').val()};

//     $.get('/api/xss.json', params, displayResult);
//     $('#pageloader').show();

//     // let table = $('#table').DataTable();
//     // table.ajax.reload();

//   });



$(document).ready(function(){
    $("#url_form").on("submit", function(){
     $("#pageloader").fadeIn();
    });//submit
});//document ready




//   $('#xss').submit(function(e){
//     e.preventDefault();
//     $.ajax({
//         url:'/api/xss.json',
//         type:'post',
//         data:$('#xss').serialize(),
//         success:function(){
//             //whatever you wanna do after the form is successfully submitted
//             alert(data)
//         }
//     });
// });

//   $.get('/api/xss.json', (response) => {
//     // Display response from the server
//     $('#url_form').text(response.toString());
//     // alert(`${response}`);
//   });

// $.get('/api/ping.json', (response) => {
//     $('#ping').text(response.toString());
//   });

//   $.get('/api/ping.json', (response) => {
//     // Display response from the server
//     alert(`${response}`);
//   });



document.getElementById("reports").onclick = function () {
    location.href = "/reports";
};

document.getElementById("dashboard").onclick = function () {
    location.href = "/";
};


