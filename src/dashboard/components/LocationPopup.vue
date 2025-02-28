<template>
  <div class="locationPopup">
    <div @click="closePopup" class="locationPopupBG">
    </div>
    <div class="locationPopupModal">
      <div class="locationPopupModalHeader">
        <div>Add Location</div>
        <button @click="closePopup">X</button>
      </div>
      <div class="locationPopupModalInput">
        <FontAwesomeIcon :icon="['fas', 'search']" class="search-icon" />
        <input v-model="locationName" type="text" placeholder="Enter location name">
        <button @click="clearInput">X</button>
      </div>
      <button class="addLocationButton" @click="handleAddLocation">Add location</button>
    </div>
  </div>
  </template>
  
  <script setup>
  
  import { ref } from 'vue';

const props = defineProps({
  createLocation: Function,
  togglePopup: Function
});

const locationName = ref('');  // Create a reactive variable for input value

// Call createLocation function with locationName when the button is clicked
const handleAddLocation = () => {
  if (locationName.value) {
    props.createLocation(locationName.value);  // Pass the location name to the function
    locationName.value = '';  // Clear the input after creating the location
  }
};

// Clear input when 'X' button is clicked in the input field
const clearInput = () => {
  locationName.value = '';
};

// Close popup (you can adjust the functionality as needed)
const closePopup = () => {
    props.togglePopup()
};
  </script>
  
  <style scoped>
    .locationPopupBG{
        background-color: black;
        opacity: 0.5;
        width: 100%;
        position: absolute;
        height: 100%;
    }
    .locationPopup{
        position: fixed;
        top: 0;
        left: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
    }
    .locationPopupModal{
        z-index: 3;
        padding: 30px;
        border-radius: 10px;
        background-color: rgb(27, 27, 29);
    }
    .locationPopupModalHeader{
        display: grid;
        grid-template-columns: 1fr auto;
        margin-bottom: 10px;
        align-items: center;
        gap: 100px;
    }
    .locationPopupModalHeader div{
        font-size: 30px;
        font-weight: 700;
    }
    .locationPopupModalHeader button{
        font-weight: 700;
        width: 28px;
        height: 28px;
        display: grid;
        align-items: center;
        justify-content: center;       
        transition: 1s; 
        background-color: rgb(37,37,40);
    }
    .locationPopupModalHeader button:hover{
        color: rgb(37,37,40);
        background-color: white;
    }
    .locationPopupModalInput input{
        font-size: 25px;
        padding-left:40px ;

    }
    .locationPopupModalInput{
        position: relative;
    }
    .locationPopupModalInput svg{
        position: absolute;
        top: 50%;
        transform: translate(10px, -50%);

    }
    .locationPopupModalInput button{
        position: absolute;
        right:0;
        top: 50%;
        font-weight: 700;
        width: 22px;
        height: 22px;
        transform: translate(-10px, -50%);
    }
    .locationPopupModalInput button:hover{
        background-color: rgb(37,37,40);
    }
    .addLocationButton{
        background-color: white;
        color: rgb(27, 27, 29);
        border-radius: 10px;
        width: 100%;
        height: 50px;
        font-size: 20px;
        margin-top: 20px;
        font-weight: 700;
        transition: 1s;
    }
    .addLocationButton:hover{
        background-color: rgb(37,37,40);
        color: white;
    }
  </style>