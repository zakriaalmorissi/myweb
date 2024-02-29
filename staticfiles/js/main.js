 
 
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

    
            
      
