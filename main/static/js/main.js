 
 
 const hamMenu = document.querySelector('.ham-menu');
        const offScreen = document.querySelector('.off-screen');
        const pageName = document.getElementById('page-name');
        hamMenu.addEventListener('click', () => {
            hamMenu.classList.toggle('active');
            offScreen.classList.toggle('active');
            pageName.classList.toggle('active');

        })
        // retrieve the dark mode setting from the local storage when the page loads 
        window.addEventListener('load',()=>{
            const darkModeEnabled = localStorage.getItem('darkMode') === 'true';
            const darkMode = document.querySelector('body');

            if (darkModeEnabled){
                darkMode.classList.add('dark');
            }
        })
        // the dark mode switch
        const toggleSwitch = document.getElementById('toggleSwitch');
        const darkMode = document.querySelector('body');

        toggleSwitch.addEventListener('click', () => {
            darkMode.classList.toggle('dark');


            // store the dark mode setting in local storage
            const darkModeEnabled = darkMode.classList.contains('dark');
            console.log(darkModeEnabled)
            localStorage.setItem('darkMode',darkModeEnabled)

        })
        //============= profile page =================================


        // upload the image to page once the user selects one 

        const fileInput = document.getElementById('fileInput');
        const imageFile = document.getElementById('imageFile');

        fileInput.addEventListener('change',function (e){
            // access the selected file from the input element
            let currentImage = e.target.files[0];
            
            // read the seleccted file and convert it into a data URL
            let reader = new FileReader();
            // display the selected file (image)
            reader.onload = function(event){
                imageFile.src = event.target.result;
               
            }
            reader.readAsDataURL(currentImage);
        })
        
        // by default disable the submit button and change its color 
        function Disable(){
            document.getElementById("submitButton").disabled = true;
            document.getElementById("submitButton").style.backgroundColor = 'gray';
            document.getElementById("submitButton").style.color = 'lightgray';
        }

        Disable()
          // get the value of user inputs 
        const userName = document.getElementById("input-name");
        const userBio = document.getElementById("user-bio");
      
        // add event listener to disable the submit button unless the user type something 
        userName.addEventListener('keyup', (e)=>{
            let currentValue = e.target.value;
            // prevent the user from submitting empty value or whitespaces 
            if (currentValue.trim() === '' ){
            
            
                Disable()

            } else  {
                // enable the button 
                let submitButton = document.getElementById("submitButton");
                submitButton.disabled = false;
                submitButton.style.backgroundColor = '#205ffefa';
                submitButton.style.color = 'white';


            }
          



        })

    
            
      
