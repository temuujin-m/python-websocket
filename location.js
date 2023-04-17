
if ("geolocation" in navigator) {
    /* geolocation is available */
    navigator.geolocation.getCurrentPosition(function(position) {
      /* location successfully obtained */
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
    }, function(error) {
      /* location error */
      console.error(`Error getting location: ${error.message}`);
    });
  } else {
    /* geolocation is not available */
    console.error("Geolocation is not supported by this browser.");
  }
  