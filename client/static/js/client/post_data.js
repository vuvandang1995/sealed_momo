$(document).ready(function(){
    $(".add_items_data").click(function(){
        $("#list_data").append('<div class="form-group row data">\
                                    <div class="col">\
                                    <input type="text" class="form-control key" placeholder="Key" required name="data_key">\
                                    </div>\
                                    <div class="col">\
                                    <input type="text" class="form-control value" placeholder="Value" required name="data_value">\
                                    </div>\
                                    <div class="col">\
                                    <button class="btn btn-danger delete_items_data" type="button">Delete</button>\
                                    </div>\
                                </div>');
    });

    $("body").on('click', '.delete_items_data', function(){
        $(this).parent().parent().remove();
    });

    // $('#encrypt').submit(function(e){
    //     var list_envs = [];
    //     var token = $("input[name=csrfmiddlewaretoken]").val();
    //     var cluster = $('#cluster').find(":selected").val();
    //     var namespace = $("input[name=namespace]").val();
    //     var secret_type = $('#secret-type').find(":selected").val();
    //     var secret_name = $("input[name=secret-name]").val();
    //     $(".data").each(function(){
    //         dict_item = {}
    //         dict_item[$(this).find(".key").val()] = $(this).find(".value").val();
    //         list_envs.push(dict_item);
    //     });
    //     $.ajax({
    //         type:'POST',
    //         url:location.href,
    //         data: {'csrfmiddlewaretoken':token, 'cluster': cluster, 'namespace': namespace, 'secret_name': secret_name, 'secret_type': secret_type, 'list_envs': JSON.stringify(list_envs)},
    //         success: function(resultData){}
    //     });
    //     // var file_data = $('#file').prop('files');
    //     // alert(typeof(file_data));
    // });

    updateList = function() {
        var input = document.getElementById('file');
        var output = document.getElementById('fileList');
        var children = "";
        for (var i = 0; i < input.files.length; ++i) {
            children += '<li>' + input.files.item(i).name + '</li>';
        }
        output.innerHTML = '<ul>'+children+'</ul>';
    }
});