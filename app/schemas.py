from typing import Literal

from pydantic import BaseModel, Field

class InvoiceData(BaseModel): 
    vendor : str | None = None
    invoice_number : str | None = None 
    invoice_date : str | None = None 
    currency : Literal["ETB", "USD", "EUR", "GBP"]

    subtotal : float | None = Field(default= None , ge = 0)
    tax : float | None = Field(default= None, ge = 0)

    total : float | None = Field(default= None , ge=0)


class ExtractionRequest(BaseModel): 
    text : str | None  = Field(min_length= 1 , max_length=200000)

class ExtractionResponse(BaseModel) : 
    data : InvoiceData
