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
                    
                    $("#table").html(txt); 
                    //#use slice function
                    // $("#table").append(txt);
                    arr.push(cur_val)
                    
                }
            }
            console.log(arr.slice(Math.max(arr.length - 5, 0)))
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