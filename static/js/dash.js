


let currentPrice = new XMLHttpRequest();
setInterval(function(){ 


    currentPrice.open('GET', 'https://api.gdax.com/products/BTC-USD/book', true);
    currentPrice.onreadystatechange = function(){
      if(currentPrice.readyState == 4){
        let ticker = JSON.parse(currentPrice.responseText);
        let price = ticker.bids[0][0];
        document.getElementById('btc').innerHTML = "₿: $" + price;
      };
    };
    currentPrice.send();


 }, 2000);


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
    let scan = document.getElementById('scan')
    let save = document.getElementById('save_report')
    let target = evt.target;
    let val = $("input[type=submit][clicked=true]").innerHTML;
    
    console.log(val);
    

    evt.preventDefault();
    $('#table').hide()
    $('#notvuln').hide()
    let params = {'url_form': $('#url').val()};
    if ($(document.activeElement).text() === "Scan") {
        $.get('/api/xss.json', params, displayResult);
        $('#pageloader').show();

    } else {
        console.log('went to else')
        $.get('/save_report')
    }

    $.get('/api/xss.json', params, displayResult);
    $('#pageloader').show();

    // let table = $('#table').DataTable();
    // table.ajax.reload();

  });




function urlcodec() {
    console.log("launched urlcodec")
    let choice = document.getElementById('choice').value;
    if (choice === "encode") {
        
        let text = document.getElementById('urlcodec_textarea').value;
        let encoded = encodeURI(text)
        document.getElementById('urlcode_output').value = encoded

    } else {
        let text = document.getElementById('urlcodec_textarea').value;
        let encoded = decodeURI(text)
        document.getElementById('urlcode_output').value = encoded

    }
}



// document.getElementById("encode").onsubmit = function () {
//     if choice == "encode" 
//     encodeURI(data)
    
// };

// document.getElementById("decode").onclick = function () {
//     $.get('/urlcode');
//     decodeURI(data)
// };

$('#flash_msg_login').hide().delay(8).fadeIn(800).delay(2000).fadeOut(800)


document.getElementById("save_report").onclick = function () {
    $('#flash_msg').removeAttr("hidden")
    setTimeout(() =>$('#flash_msg').attr("hidden", true), 1500)
}


document.getElementById("scan").onclick = function () {
    console.log("getting called")
    $('#scanning').removeAttr("hidden")
    setTimeout(() =>$('#scanning').attr("hidden", true), 1500)
}