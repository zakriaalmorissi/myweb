 
 
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

    
            
import {useEffect, useState} from 'react';
import React, {Component} from 'react';
import {fetchData, ErrorResponse} from '../network/api.ts';
import { Item } from '../network/models.ts';
import { url } from '../network/constants.js';
;


// Learn Callbacks in react and javascripts with broader details
function Home () {
    const [foods, setFood] = useState([]);
    const [errorMessage, setErrorMessage] = useState({status: null, error: null, message: null});
    
    // go more about function and keyword arguements
        useEffect(()=> {getAllData(`${url}home`)}, []);
    
        async function getAllData (url: string) {
            let errorResponse;

            await fetchData<Item, Error>(url, { // i think the problem was the await function 
                getData: (data) => { setFood(data) },
                apiError: (res) => { errorResponse = res }
            }
            )
            if (errorResponse !== undefined) setErrorMessage(errorResponse);
        }

    return <>
        <Items foods={foods}/>
        <div>
            {errorMessage.message}
        </div>
    </>
}



function Items (props) {
    const foods = props.foods;

    return <>
        <div>
            {
                foods.map((food: Item)=> {
                    return  <div key={food.id}>
                        {food.name}
                    </div>
                })
            }
        </div>
        <div>
        </div>
    </>
}


export  default Home;  export interface SuccessResponse<T> {
    status: string;
    data: T;
    
}

export interface ErrorResponse<E> {
    status: string;
    error: E;
    message?: string; 

}

export interface Error {
    code: 'string';
    
}





// how to make a call
async function fetchData<T, E>( url: string, { getData, apiError}: {
    getData: (data: SuccessResponse<T>)=> void,
    apiError: (response: ErrorResponse<E>) => void
}): Promise<void> {
    try {
            // fecth data from the api 
            const response = await fetch(url);
            // check the response state
            if (response.ok){
                const data = await response.json();
                getData(data);
            } 

        } catch (error) {
                apiError({status: "error", message: "network error", error: error});

        }}

async function postData<T, E>(url: string, {data, getResponse}:{
    data: T,
    getResponse: (response: SuccessResponse<T> | ErrorResponse<E>) => void;
}
):Promise<void>{
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                'content-type': 'application/json' 
            }
        })
        const responseData: T | E = await response.json();
        if (response.ok) {
            getResponse({status: "ok", data: responseData as T});
        }
        else if (response.status === 400) { 
            getResponse({status:"Bad request", error: responseData as E, message: "Format error"
            });
        }

    } catch (error) {
        getResponse({status: "error", message: "network error", error: error});
      
    }  
}

export {fetchData, postData};  
