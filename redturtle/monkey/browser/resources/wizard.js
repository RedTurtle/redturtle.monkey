require([
  'jquery',  
  'mockup-i18n',
  'mockup-patterns-sortable'
], function($, I18n, Sortable) {
     'use strict';
     var i18n = new I18n();
     debugger
     const domain = 'redturtle.monkey';
     i18n.loadCatalog(domain);
     var _ = i18n.MessageFactory(domain);
     $('.toggle-checkbox').click(function(){
        var $checkbox = $(this).closest('table').find('tbody :checkbox');
            $checkbox.attr('checked', $(this).attr('checked'));
     });
     $('#wizard').smartWizard(
     {
          transitionEffect:'slideleft',
          onLeaveStep:leaveAStepCallback,
          onFinish:onFinishCallback,
          enableFinishButton:false,
          labelNext: _('Next'), // label for Next button
          labelPrevious: _('Previous'), // label for Previous button
          labelFinish: _('Send')
          }
     );
     function leaveAStepCallback(obj){
        var step_num= obj.attr('rel');
        return validateSteps(step_num);
     }
     function onFinishCallback(){
       if(validateSteps(2)){
         $('form').submit();
       }
       else{
         return false;
       }
     }
     // $('#step-1 tbody').sortable({
     //   items: "> tr",
     //   appendTo: "parent",
     //   helper: "clone"
     // }).disableSelection();

 function validateSteps(step){
         var isStepValid = true;
         if(step == 1){
           if(validateStep1() == false ){
               isStepValid = false;
               $('#wizard').smartWizard('showMessage','Please select at least one item.');
               $('#wizard').smartWizard('setError',{stepnum:step,iserror:true});
           }else{
               $('#wizard').smartWizard('setError',{stepnum:step,iserror:false});
           }
       }
         if(step == 2){
           if(validateStep2() == false ){
               isStepValid = false;
               $('#wizard').smartWizard('showMessage','Please fill required fields.');
               $('#wizard').smartWizard('setError',{stepnum:step,iserror:true});
           }else{
               $('#wizard').smartWizard('setError',{stepnum:step,iserror:false});
           }
       }
         return isStepValid;
 }

 function validateStep1(){
   var isValid = true;
   // Validate items
   var size = $('tbody :checkbox:checked').size()
   if(!size && size == 0){
     isValid = false;
   }
   return isValid;
  }
  function validateStep2(){
    var isValid = true;
    // Validate form
    var un = $('input[name="campaign_title"]').val();
    if(!un && un.length <= 0){
      isValid = false;
    }
    var un = $('input[name="campaign_description"]').val();
    if(!un && un.length <= 0){
      isValid = false;
    }
    return isValid;
   }
 });
