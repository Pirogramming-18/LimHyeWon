
//fetch items from json file
function loadItems(){
    return fetch('./data/data.json')
    .then(response=>response.json())
    .then(json=>json.items);

}
//update list with given items
function displayItems(items){
    const container=document.querySelector('.items');
    container.innerHTML=items.map(item=>createHTMLString(item)).join('');

}

//create html list item from given data item
function createHTMLString(item){
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
        <span class="item__descriptioin">${item.gender},${item.size}</span>
    </li>
    `;
}

//main
loadItems()
.then(items=>{
    console.log(items);
    displayItems(items);
    // setEventListeners(items);
})
.catch(console.log);