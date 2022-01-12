
from src.main.service.RecordService import RecordService
from src.main.infra.datasource.RecordRepositoryDataSourceImple import RecordRepositoryDataSourceImple
from src.main.domain.dto.RecordResultDto import RecordResultDto
from datetime import datetime, timedelta
from src.main.domain.Record import Record
import pytest

recordRepository = RecordRepositoryDataSourceImple()
recordService = RecordService(recordRepository)

@pytest.fixture
def add_test_income():
    recordRepository.create(Record("08800140600090", (datetime.now()- timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'), "허리바로", "kim", "출고"))
    recordRepository.create(Record("08800140600090", (datetime.now()- timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),"허리바로", "kim", "입고"))

def test_succes_read_record():
    # given
    userId = "kim"
    records = recordRepository.readAll(id)
    expected = RecordResultDto(True, "Getting Record List!", records)
    
    # when
    actual = recordService.recordService(id)

    # then
    assert actual == expected
