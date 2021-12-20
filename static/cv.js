function validate() {
      
        if( document.Form.FName.value == "" ) {
           alert( "Please provide your first name!" );
           document.Form.FName.focus() ;
           return false;
        }
        if( document.Form.LName.value == "" ) {
           alert( "Please provide your last name!" );
           document.Form.LName.focus() ;
           return false;
        }
        if( document.Form.Email.value == "" ) {
            alert( "Please provide your Email!" );
            document.Form.Email.focus() ;
            return false;
         }
        return( true );
     }

function showText(Item2Det)  {
        document.getElementById(Item2Det).style.display = "block";
}