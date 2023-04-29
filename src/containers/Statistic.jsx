import React, { useState } from 'react'
import { Button, DatePicker, Select, Space } from 'antd';
import '../App.scss'

// import Axios from 'axios';
import axios from "axios";



const { RangePicker } = DatePicker;

const navBarOptions = [
    {
        value: 1,
        label: "Hàm thống kê 1"
    },
    {
        value: 2,
        label: "Hàm thống kê 2"
    },
    {
        value: 3,
        label: "Hàm thống kê 3"
    },
    {
        value: 4,
        label: "Hàm thống kê 4"
    },
    {
        value: 5,
        label: "Hàm thống kê 5"
    },
    {
        value: 6,
        label: "Hàm thống kê 6"
    },
    {
        value: 7,
        label: "Hàm thống kê 7"
    },
    {
        value: 8,
        label: "Hàm thống kê 8"
    },
    {
        value: 9,
        label: "Hàm thống kê 9"
    },
    {
        value: 10,
        label: "Hàm thống kê 10"
    },
    {
        value: 11,
        label: "Hàm thống kê 11"
    },
    {
        value: 12,
        label: "Hàm thống kê 12"
    },
]


const Statistic = () => {
    const [statType,setStatType] = useState(localStorage.getItem("statType") ? parseInt(localStorage.getItem("statType")) : 1);

    const [imageSrc1,setImageSrc1] = useState();
    const [imageSrc2,setImageSrc2] = useState();
    const [imageSrc3,setImageSrc3] = useState();
    const [imageSrc4,setImageSrc4] = useState();
    const [imageSrc5,setImageSrc5] = useState();
    const [imageSrc6,setImageSrc6] = useState();
    const [imageSrc7,setImageSrc7] = useState();
    const [imageSrc8,setImageSrc8] = useState();
    const [imageSrc9,setImageSrc9] = useState();
    const [imageSrc10,setImageSrc10] = useState();
    const [imageSrc11,setImageSrc11] = useState();
    const [imageSrc12,setImageSrc12] = useState();

    const [startDate,setStartDate] = useState();
    const [endDate,setEndDate] = useState();
    const [year,setYear] = useState();
    const [startYear, setStartYear] = useState();
    const [endYear, setEndYear] = useState();

    const fetchStatistic = () => {
        axios.defaults.baseURL = 'http://127.0.0.1:8000';


        if(statType===1){
            var config = {
                method: 'post',
                url: '/visualization/1/',
                data : {
                    start_date: new Date(startDate).toLocaleDateString('sv'),
                    end_date: new Date(endDate).toLocaleDateString('sv'),
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)
              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===4){
            var config = {
                method: 'post',
                url: '/visualization/4/',
                data : {
                    start_date: new Date(startDate).toLocaleDateString('sv'),
                    end_date: new Date(endDate).toLocaleDateString('sv'),
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===2){
            var config = {
                method: 'post',
                url: '/visualization/2/',
                data : {
                    year: new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)
              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===5){
            var config = {
                method: 'post',
                url: '/visualization/5/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===7){
            var config = {
                method: 'post',
                url: '/visualization/7/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===8){
            var config = {
                method: 'post',
                url: '/visualization/8/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===9){
            var config = {
                method: 'post',
                url: '/visualization/9/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===10){
            var config = {
                method: 'post',
                url: '/visualization/10/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===11){
            var config = {
                method: 'post',
                url: '/visualization/11/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===12){
            var config = {
                method: 'post',
                url: '/visualization/12/',
                data : {
                    year:  new Date(year).getFullYear()
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===3){
            var config = {
                method: 'post',
                url: '/visualization/3/',
                data : {
                    start_year: startYear,
                    end_year: endYear
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        else if(statType===6){
            var config = {
                method: 'post',
                url: '/visualization/6/',
                data : {
                    start_year: startYear,
                    end_year: endYear
                }
            };
            return axios(config).then( (response) => {
                handleInsertImage(response)

              })
              .catch(function (error) {
                console.log(error);
              });
        }
        
        

        
    };

    const handleInsertImage = (response) => {
        const urlImage = response.data.url_image;
        setTimeout(()=>{
            const cloneImage = require(`../image_visualization/${urlImage}`)
            switch (statType) {
                case 1:
                    setImageSrc1(cloneImage);
                  break;
                case 2:
                    setImageSrc2(cloneImage);
                  break;
                case 3:
                    setImageSrc3(cloneImage);
                  break;
                case 4:
                    setImageSrc4(cloneImage);
                  break;
                case 5:
                    setImageSrc5(cloneImage);
                  break;
                case 6:
                    setImageSrc6(cloneImage);
                  break;
                case 7:
                    setImageSrc7(cloneImage);
                    break;

                  case 8:
                    setImageSrc8(cloneImage);
                    break;

                case 9:
                    setImageSrc9(cloneImage);
                    break;

                  case 10:
                    setImageSrc10(cloneImage);
                    break;

                  case 11:
                    setImageSrc11(cloneImage);
                    break;

                  case 12:
                    setImageSrc12(cloneImage);
                    break;


              }
        }, 5000);

        
        console.log(response);
        
    }

    const handleChangeStatistic = () => {

    }

    const handleDateRangePicker = (event) => {
        console.log(event)
        setStartDate(event[0].$d);
        setEndDate(event[1].$d);
    }

    const handleYearPicker = (event) => {
        setYear(event)
    }

    const handleYearRangePicker = (event) => {
        console.log(event)
        setStartYear(event[0].$y
            )
        setEndYear(event[1].$y
            )
    }

    const handleChangeStatType = (type) => {
        setStatType(type)
        setImageSrc1(undefined)
        setImageSrc2(undefined)
        setImageSrc3(undefined)
        setImageSrc4(undefined)
        setImageSrc5(undefined)
        setImageSrc6(undefined)
        setImageSrc7(undefined)
        setImageSrc8(undefined)
        setImageSrc9(undefined)
        setImageSrc10(undefined)
        setImageSrc11(undefined)
        setImageSrc12(undefined)
        localStorage.setItem("statType",type)
        window.location.reload()

        // const element = document.getElementById("statistic-image");
        // element.remove();

        // var child = document.createElement('div');
        // child.innerHTML = "<img id='statistic-image' src={imageSrc}/>";

        // var parent = document.getElementById("statistic-image-father");

        // parent.appendChild(child);
    }


    return (
        <div className='statistic-main'>
            <div className='nav-bar'>
                {
                    navBarOptions.map(item=>(
                        <div className={`nav-item ${item.value === statType ? "active-nav-item" : ""}`} onClick={()=> handleChangeStatType(item.value)}>
                            {item.label}
                        </div>
                    ))
                }
               
            </div>
            <div className='statistic-content'>
                <div className='select-area'>
                    {
                        (statType===1 || statType===4) && 
                        <RangePicker 
                            className='range-picker'
                            onChange={
                                (val) => handleDateRangePicker(val)
                            }
                        />
                    }
                    {
                        (statType===2 || statType===5 || statType === 7 || statType === 8|| statType === 9 || statType === 10 || statType === 11 || statType === 12) && 
                        <DatePicker className="year-picker" picker="year"  onChange={
                            (val) => handleYearPicker(val)
                        }/>
                    }
                    {
                        (statType===3 || statType===6) && 
                        <RangePicker className='year-range-picker' picker="year" onChange={
                            (val) => handleYearRangePicker(val)
                        }/>
                    }
                    <Button
                        onClick={fetchStatistic}
                    >Xem thống kê</Button>
                </div>
                <div id='statistic-image-father' className='statistic-diagram'>
                    {
                        imageSrc1 &&
                        <img id='statistic-image' src={imageSrc1}/>

                    }
                    {
                        imageSrc2 &&
                        <img id='statistic-image' src={imageSrc2}/>

                    }
                    {
                        imageSrc3 &&
                        <img id='statistic-image' src={imageSrc3}/>

                    }
                    {
                        imageSrc4 &&
                        <img id='statistic-image' src={imageSrc4}/>

                    }
                    {
                        imageSrc5 &&
                        <img id='statistic-image' src={imageSrc5}/>

                    }
                    {
                        imageSrc6 &&
                        <img id='statistic-image' src={imageSrc6}/>

                    }
                    {
                        imageSrc7 &&
                        <img id='statistic-image' src={imageSrc7}/>

                    }
                    {
                        imageSrc8 &&
                        <img id='statistic-image' src={imageSrc8}/>

                    }
                    {
                        imageSrc9 &&
                        <img id='statistic-image' src={imageSrc9}/>

                    }
                    {
                        imageSrc10 &&
                        <img id='statistic-image' src={imageSrc10}/>

                    }
                    {
                        imageSrc11 &&
                        <img id='statistic-image' src={imageSrc11}/>

                    }
                    {
                        imageSrc12 &&
                        <img id='statistic-image' src={imageSrc12}/>

                    }
                </div>
            </div>
        </div>
    )
}

export default Statistic

