// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.civo.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetDatabaseVersionFilter {
    /**
     * @return Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    private @Nullable Boolean all;
    /**
     * @return Filter versions by this key. This may be one of `default`, `engine`, `version`.
     * 
     */
    private String key;
    /**
     * @return One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    private @Nullable String matchBy;
    /**
     * @return Only retrieves `versions` which keys has value that matches one of the values provided here
     * 
     */
    private List<String> values;

    private GetDatabaseVersionFilter() {}
    /**
     * @return Set to `true` to require that a field match all of the `values` instead of just one or more of them. This is useful when matching against multi-valued fields such as lists or sets where you want to ensure that all of the `values` are present in the list or set.
     * 
     */
    public Optional<Boolean> all() {
        return Optional.ofNullable(this.all);
    }
    /**
     * @return Filter versions by this key. This may be one of `default`, `engine`, `version`.
     * 
     */
    public String key() {
        return this.key;
    }
    /**
     * @return One of `exact` (default), `re`, or `substring`. For string-typed fields, specify `re` to match by using the `values` as regular expressions, or specify `substring` to match by treating the `values` as substrings to find within the string field.
     * 
     */
    public Optional<String> matchBy() {
        return Optional.ofNullable(this.matchBy);
    }
    /**
     * @return Only retrieves `versions` which keys has value that matches one of the values provided here
     * 
     */
    public List<String> values() {
        return this.values;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDatabaseVersionFilter defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean all;
        private String key;
        private @Nullable String matchBy;
        private List<String> values;
        public Builder() {}
        public Builder(GetDatabaseVersionFilter defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.all = defaults.all;
    	      this.key = defaults.key;
    	      this.matchBy = defaults.matchBy;
    	      this.values = defaults.values;
        }

        @CustomType.Setter
        public Builder all(@Nullable Boolean all) {

            this.all = all;
            return this;
        }
        @CustomType.Setter
        public Builder key(String key) {
            if (key == null) {
              throw new MissingRequiredPropertyException("GetDatabaseVersionFilter", "key");
            }
            this.key = key;
            return this;
        }
        @CustomType.Setter
        public Builder matchBy(@Nullable String matchBy) {

            this.matchBy = matchBy;
            return this;
        }
        @CustomType.Setter
        public Builder values(List<String> values) {
            if (values == null) {
              throw new MissingRequiredPropertyException("GetDatabaseVersionFilter", "values");
            }
            this.values = values;
            return this;
        }
        public Builder values(String... values) {
            return values(List.of(values));
        }
        public GetDatabaseVersionFilter build() {
            final var _resultValue = new GetDatabaseVersionFilter();
            _resultValue.all = all;
            _resultValue.key = key;
            _resultValue.matchBy = matchBy;
            _resultValue.values = values;
            return _resultValue;
        }
    }
}
