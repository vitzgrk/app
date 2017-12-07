$(document).ready(function(){
    $("#btn").click(function(){
        var inn = parseInt($('#inn').val())
        var name = $('#name').val()
        var balance = parseFloat($('#balance').val()).toFixed(2)
        console.info(name.length < 2)
        if (isNaN(inn) || isNaN(balance) || name.length < 2){
            alert("Введите корректные данные")
        } else {
        $.ajax({
            type: 'POST',
            url : '/module/ajax/createUser/',
            data : {
                'name': name,
                'email': $('#email').val(),
                'inn': inn,
                'balance': balance,
            },
            success: function(data){
                alert(data.status)
                location.reload()
            }
        })
        }
    });
    $.ajax({
        type: 'GET',
        url : '/module/ajax/show/',
        success: function(data){
            data.forEach(element => {
                $('#from').append('<option>'+element.name+'</option>')
                $('#to').append('<option>'+element.name+'</option>')
                $('#table tr:last').after('<tr><td>'+element.name+'</td><td>'+element.inn+'</td><td>'+element.email+'</td><td>'+element.balance+'</td></tr>')
            });
            
        }
    })
    $('#from').on('change', ()=>{
        $.ajax({
            type: 'POST',
            url : '/module/ajax/getUserInfo/',
            data : {
                'name': $('#from').val()
            },
            success: function(data){
                $('#info_name').text('Имя: '+data.name)
                $('#info_inn').text('ИНН: '+data.inn)
                $('#info_email').text('EMAIL: '+data.email)
                $('#info_balance').text('БАЛАНС: '+data.balance)
                $('#amount').show()
                $('#btn1').show()
            }
        })
    })

    $('#btn1').click(function(){
        var amount = parseFloat($('#amount').val())
        var from_name = $('#from').val()
        // var to_name = $('#to').val()
        var inns = $('#inns').val().split(',')
        console.log(inns)
        if (isNaN(amount) || amount < 0) {
            alert("Введите правильную сумму!")
        }else {
            console.info(amount)
            $.ajax({
                type: 'POST',
                url : '/module/ajax/checkBalance/',
                data : {
                    'from_name' : from_name,
                    'inns' : JSON.stringify(inns),
                    'amount': amount
                },
                success: function(data){
                    alert(data.status)
                    location.reload()
                }
            })
        }
    })    

})