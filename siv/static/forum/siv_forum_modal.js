var modal;
function open_modal(url, document){
    console.log('Entro a la funcion')
    modal = $(document).dialog({
        title: "Yo pienso que...",
        modal: true,
        width: 500,
        resizable: false,
        draggable: false,
        dialogClass: 'no-close',
        open: function() {
            $('.ui-widget-overlay').addClass('custom-overlay');
        }
    }).dialog('open').load(url)
    console.log('[MODAL]: ', modal)
}

function close_modal()
{
    modal.dialog("close");
}

