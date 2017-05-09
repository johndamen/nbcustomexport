// file nbcustomexport.js

define([
    'base/js/namespace'
], function(
    Jupyter
) {
    function load_ipython_extension() {
        function add_custom_formats(items, state){
            console.log('items', items)
            var $dlMenu = $("#download_html").parent();
            items.map(function(format){
                console.log('format', format)
                $("<li/>", {"id": "download_" + format.key})
                    .append(
                        $("<a/>", {"href": "#"})
                            .text(format.label)
                            .on("click", function(){ Jupyter.menubar._nbconvert(format.key, true); })
                    )
                .appendTo($dlMenu)
            })
        }

        $.get(Jupyter.notebook.base_url + "nbcustomexport/list", add_custom_formats);
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});