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





// $.get('/api/ping.json', (response) => {
//     $('#ping').text(response.toString());
//   });

//   $.get('/api/ping.json', (response) => {
//     // Display response from the server
//     alert(`${response}`);
//   });