
window.setInterval(function(){
    $.get('/api/ping.json', (data) => {
        // alert(JSON.stringify(data));



        if(data){
            var len = data.length;
            var txt = "";
            if(len > 0){
                for(var i=0;i<len;i++){
                    if(data[i].time && data[i].source_ip){
                        txt += "<tr><td>"+data[i].time+"</td><td>"+data[i].source_ip+"</td></tr>";
                    }
                }
                if(txt != ""){
                    $("#table").append(txt);
                }
            }
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
