// PART 1

var students = [
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
];

function getNames(students){

    for(var i in students){
        console.log(students[i].first_name + " " + students[i].last_name);
    }
}

getNames(students);

// PART 2

var users = {
    'Students': [
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
    ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
    ]
};

function getNames2(users) {

    var indent = " - ";
    var space = " ";

    //console.log(users["Students"][0].first_name)

    for (var i in users){

        console.log(i);
        var counter = 0;

        for(var k in users[i]){
            counter += 1;
            console.log(counter+indent+users[i][k].first_name+space+users[i][k].last_name+indent+(users[i][k].first_name.length+users[i][k].last_name.length));
        }
    }
}
getNames2(users); 