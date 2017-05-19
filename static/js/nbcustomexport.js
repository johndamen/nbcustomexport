// file nbcustomexport.js

define([
    'base/js/namespace'
], function(
    Jupyter
) {
    function load_ipython_extension() {

        // add formats to menu
        function add_custom_formats(data){
            // get menu element as parent of existing
            var $dlMenu = $("#download_html").parent();
            // create new elements with click callback
            data.templates.map(function(format){
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
