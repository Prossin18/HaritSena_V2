const rewardsWrapper = document.querySelector('.rewards-wrapper');
const prevButton = document .querySelector('.reward-nav.prev');
const nextButton = document .querySelector('.reward-nav.next');

// console.log("Wrapper: ", rewardsWrapper);
// console.log("Previous: ", prevButton);
// console.log("Next: ", nextButton);

if(rewardsWrapper && prevButton && nextButton)
    // agar yeh tinho buttons presetn hiann ..page par to next code apply karo
{
    nextButton.addEventListener('click',function() {
        rewardsWrapper.scrollBy({
            left:205,
            behavior:'smooth'
        });
    });

     prevButton.addEventListener('click',function() {
        rewardsWrapper.scrollBy({
            left:-205,
            behavior:'smooth'
        });
    });
}


