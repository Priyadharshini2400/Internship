  document.addEventListener('DOMContentLoaded', function () {
  const track = document.querySelector('.carousel-track');
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const cards = document.querySelectorAll('.review-card');
  const cardsPerSlide = 3;

  const cardMargin = 25; 
  const cardWidth = cards[0].offsetWidth + cardMargin;
  const totalCards = cards.length;
  const maxIndex = Math.ceil(totalCards / cardsPerSlide) - 1;

  let currentIndex = 0;

  function updateCarousel() {
    track.style.transform = `translateX(-${currentIndex * cardWidth * cardsPerSlide}px)`;
  }

  nextBtn.addEventListener('click', () => {
    if (currentIndex < maxIndex) {
      currentIndex++;
      updateCarousel();
    }
  });

  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      updateCarousel();
    }
  });
});

function updateCarousel() {
  const scrollDistance = (cardWidth + gap) * currentIndex;
  track.style.transform = `translateX(-${scrollDistance}px)`;
  nextBtn.disabled = currentIndex >= maxIndex;
  prevBtn.disabled = currentIndex === 0;
}


//onway


 function toggleDropdown() {
    const dropdown = document.getElementById("dropdownOptions");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
  }

  function selectOption(value) {
    document.getElementById("selectedOption").innerText = value;
    document.getElementById("dropdownOptions").style.display = "none";
  }


  document.addEventListener("click", function (event) {
    const dropdown = document.querySelector(".custom-select");
    if (!dropdown.contains(event.target)) {
      document.getElementById("dropdownOptions").style.display = "none";
    }
  });

  
//min

  document.addEventListener("DOMContentLoaded", function () {
    const selectedTime = document.getElementById("selectedTime");
    const dropdown = document.getElementById("dropdownTimeOptions");

    selectedTime.addEventListener("click", function (e) {
      e.stopPropagation();
      dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    });

    window.selectTime = function (value) {
      selectedTime.innerText = value;
      dropdown.style.display = "none";
    };

    window.addEventListener("click", function (e) {
      if (!document.getElementById("extraTimeSelect").contains(e.target)) {
        dropdown.style.display = "none";
      }
    });
  });




 let navbar = document.querySelector(".nav-ul");
let navbtn = document.getElementById("ellips");

if (navbtn && navbar) {
  navbtn.addEventListener('click', () => {
    navbar.classList.toggle('active');
  });
}

