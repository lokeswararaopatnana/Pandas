# import pandas
# a=pandas.read_csv("C:\\Users\PATNANA LOKESWARARAO\Dropbox\Python Practice Sessions\Pandas\hi.csv")
# print(a)
# print(a.shape)  # this method shows that how many rows and columns have
# print(a.head()) # this method shows that first 5 rows and columns
# print(a.tail()) # this method shows that last 5 rows and columns
# print(a.head(2))
# print(a.tail(2))
# print(a[:])  # it will shows that all columns and rows
# print(a[2:5])
# print(a[1:3])
# print(a.columns)
# print(a.Age)
# print(a[["Name","Age"]])
# print(a['Age'].max())
# print(a['Age'].min())
# print(a.describe())
# print(a[a.Id>402])
# print(a["Name"][a.Age>15])
# print(a[a.Height<5.0])
# print(a[a.Height==a.Height.max()])
# print(a)
# b=a.set_index('Id')
# print(b)
# print(a.loc[2])

# print(dir(pandas))
print(len(['BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 
'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 'Float64Dtype', 'Float64Index', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype',
 'Int32Dtype', 'Int64Dtype', 'Int64Index', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 'NamedAgg', 
 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp',
  'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt64Index', 'UInt8Dtype', '__all__', '__builtins__', '__cached__', '__deprecated_num_index_names', 
  '__dir__', '__doc__', '__docformat__', '__file__', '__getattr__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 
  '__version__', '_config', '_is_numpy_dev', '_libs', '_testing', '_typing', '_version', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core',
   'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna',
    'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas',
     'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 
     'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata',
      'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 
      'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long']))