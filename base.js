$(function() {
    // チェックボックスのクリックを無効化します。
    $('.image_box .disabled_checkbox').click(function() {
        return false;
    });

    // 画像がクリックされた時の処理です。
    $('img.thumbnail').on('click', function() {
        if (!$(this).is('.checked')) {
            // チェックが入っていない画像をクリックした場合、チェックを入れます。
            $(this).addClass('checked');
        } else {
            // チェックが入っている画像をクリックした場合、チェックを外します。
            $(this).removeClass('checked')
        }
    });
});

function generate(){
    var output_list = [];
    var key_list = [];
    var tb = document.getElementById("output");
    var checked_elements = document.getElementsByClassName("checked") ;
    for(var i=0; i<checked_elements.length; i++){
        key_list.push(checked_elements[i].src);
    }
    console.log(JSON.stringify(key_list));
    for(var i=0; i<key_list.length; i++){
        output_list.push(url_dict[key_list[i]]);
    }
    tb.innerText = JSON.stringify(output_list).replace( /"/g , "\\\"" ) ;;
}