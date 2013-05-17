var gpio = require("gpio");
var gpio7, gpio17, intervalTimer;

// Flashing lights if LED connected to GPIO7
gpio7 = gpio.export(7, {
   ready: function() {
      inervalTimer = setInterval(function() {
         gpio7.set();
         setTimeout(function() { gpio7.reset(); }, 500);
      }, 1000);
   }
});

// Lets assume a different LED is hooked up to pin 17, the following code 
// will make that LED blink inversely with LED from pin 7 
gpio17 = gpio.export(17, {
   ready: function() {
      // bind to gpio7's change event
      gpio7.on("change", function(val) {
         gpio17.set(1 - val); // set gpio17 to the opposite value
      });
   }
});

// reset the headers and unexport after 10 seconds
setTimeout(function() {
   clearInterval(intervalTimer);          // stops the voltage cycling
   gpio7.removeAllListeners('change');   // unbinds change event
   gpio7.reset();                        // sets header to low
   gpio7.unexport();                     // unexport the header

   gpio17.reset();
   gpio17.unexport(function() {
      // unexport takes a callback which gets fired as soon as unexporting is done
      process.exit(); // exits your node program
   });
}, 10000)
