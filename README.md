# nbcustomexport
add exports for custom templates to jupyter notebooks

install using:

    jupyter nbextension install --py nbcustomexport
    jupyter nbextension enable --py nbcustomexport
    jupyter serverextension enable --py nbcustomexport
    
add templates to `nbcustomexport/templates` using the `.tpl` extension to automatically add them to the notebook exports

the menu is updated when starting the jupyter notebook server